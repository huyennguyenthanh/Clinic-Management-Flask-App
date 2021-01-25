DROP TRIGGER IF EXISTS num_patient_update ON histories;
CREATE OR REPLACE FUNCTION increase_num_patients()
	RETURNS TRIGGER
	LANGUAGE PLPGSQL
	AS 
$$
BEGIN
	IF (OLD.is_paid = FALSE AND NEW.is_paid = TRUE) THEN
		raise notice 'OLD is %', OLD.is_paid;
		IF(EXTRACT(year from NEW.date_time) NOT IN (SELECT DISTINCT which_year from salary_table)) THEN
			INSERT INTO salary_table VALUES 
			(NEW.doctor_id,EXTRACT(month from NEW.date_time),EXTRACT(year from NEW.date_time),1,6000000+0.2*NEW.total_price);

		ELSIF (EXTRACT(month from NEW.date_time) NOT IN (SELECT DISTINCT which_month from salary_table WHERE which_year = EXTRACT(year from NEW.date_time))) THEN
			INSERT INTO salary_table VALUES 
			(NEW.doctor_id,EXTRACT(month from NEW.date_time),EXTRACT(year from NEW.date_time),1,6000000+0.2*NEW.total_price);
			
		ELSIF (NEW.doctor_id NOT IN (SELECT DISTINCT doctor_id from salary_table)) THEN
			INSERT INTO salary_table VALUES 
			(NEW.doctor_id,EXTRACT(month from NEW.date_time),EXTRACT(year from NEW.date_time),1,6000000+0.2*NEW.total_price);
			
		ELSE 
			UPDATE salary_table
			SET num_patient = num_patient + 1,
			salary = salary + 0.2*NEW.total_price
			WHERE (doctor_id = NEW.doctor_id AND
			which_year = EXTRACT(year from NEW.date_time) AND
			which_month = EXTRACT(month from NEW.date_time));
		END IF;
			
	END IF;
	RETURN NEW;
END;
$$;

CREATE TRIGGER num_patient_update
AFTER UPDATE OF is_paid ON histories
FOR EACH ROW 
EXECUTE PROCEDURE increase_num_patients();


/*****************************************************************************************************************************/

CREATE OR REPLACE FUNCTION change_stock_quantity()
	RETURNS TRIGGER
	LANGUAGE PLPGSQL
	AS 
$$
BEGIN 
	IF ( ((select stock_quantity from medicines where medicine_id = NEW.medicine_id) - NEW.quantity) < 0) THEN
		DELETE FROM pre_medicines WHERE (prescription_id = NEW.prescription_id AND medicine_id = NEW.medicine_id);
		RAISE notice 'NOt enough! ';
	ELSE 
		UPDATE medicines
		SET stock_quantity = stock_quantity - NEW.quantity
		WHERE medicine_id = NEW.medicine_id;

	END IF;
	RETURN NEW;
END;
$$;

CREATE TRIGGER quantity_change
AFTER INSERT ON pre_medicines
FOR EACH ROW
EXECUTE PROCEDURE change_stock_quantity();


