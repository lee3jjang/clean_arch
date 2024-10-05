from .create_person_mutation import CreatePersonMutation
from .edit_person_mutation import EditPersonMutation
from .delete_person_mutation import DeletePersonMutation


class PersonMutations:
    create_person = CreatePersonMutation.Field()
    edit_person = EditPersonMutation.Field()
    delete_person = DeletePersonMutation.Field()
