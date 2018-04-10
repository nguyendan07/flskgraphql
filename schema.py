import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Department, Employee


class DepartmentType(SQLAlchemyObjectType):
    class Meta:
        model = Department
        interfaces = (relay.Node, )


class EmployeeType(SQLAlchemyObjectType):
    class Meta:
        model = Employee
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(EmployeeType)


schema = graphene.Schema(query=Query)
