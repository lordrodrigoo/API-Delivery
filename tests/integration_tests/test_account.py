#pylint: disable=redefined-outer-name
#pylint: disable=unused-argument
#pylint: disable=unused-import
from datetime import datetime
import pytest
from src.infra.db.entities.account import AccountEntity
from tests.integration_tests.test_user import fake_user


@pytest.fixture
def fake_account(db_session, fake_user):
    account = AccountEntity(
        user_id=fake_user.id,
        username="ana_silva",
        password_hash="hashed_password",
        status="active",
        created_at=datetime.now(),
        updated_at=None
    )
    db_session.add(account)
    db_session.commit()
    return account


def test_create_account(db_session, fake_user, fake_account):
    assert fake_account.id is not None
    assert fake_account.username == "ana_silva"
    assert fake_account.user_id == fake_user.id


def test_update_account(db_session, fake_user, fake_account):
    fake_account.username = "ana_souza"
    db_session.commit()

    updated_account = db_session.query(AccountEntity).filter_by(id=fake_account.id).first()
    assert updated_account.username == "ana_souza"

def test_relationship_between_user_and_account(db_session, fake_user, fake_account):
    pass


def test_delete_account(db_session, fake_account):
    db_session.delete(fake_account)
    db_session.commit()

    deleted_account = db_session.query(AccountEntity).filter_by(id=fake_account.id).first()
    assert deleted_account is None
