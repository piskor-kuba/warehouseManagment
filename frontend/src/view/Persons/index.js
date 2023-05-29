import { PersonsCreate } from './PersonsCreate';
import { PersonsEdit } from './PersonsEdit';
import { PersonsList } from './PersonsList';

const Persons = {
	list: PersonsList,
	create: PersonsCreate,
	edit: PersonsEdit,
};
export default Persons;
