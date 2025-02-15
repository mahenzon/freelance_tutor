import pytest

from api_v1.subject import crud as crud_subject
from api_v1.user import crud as crud_user
from api_v1.subject.schemas import CreateSubject
from core import db_helper

@pytest.fixture(autouse=True, scope='session')
async def create_subject():
    subject_in = CreateSubject(name='informatics')

    async with db_helper.session_factory() as session:
        await crud_subject.create_subject(session=session, subject_in=subject_in)


@pytest.mark.usefixtures('create_subject')
@pytest.fixture(scope='session')
async def add_subject_by_tutor(register_tutor):
    subject_names = ['informatics']
    user_id = register_tutor['id']
    async with db_helper.session_factory() as session:
        await crud_user.add_subjects_by_user(
            session=session,
            subjects=subject_names,
            user_id=user_id
        )

