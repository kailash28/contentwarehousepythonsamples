import AddDocumentToFolder
import CreateFolder
import CreateFolderObjectByFolderSchemaId
import CreateSchema
import DeleteDocument
import GetDocument
import GetSchemaList
import GetSchemaById
import DeleteSchema
import CreateDocument
import os

import ListDocumentUnderFolder
import RemoveDocumentFromFolder
import Search
import UpdateDocument
import UpdateSchema

project_number = '<projectId>'
location = 'us'  # Format is 'us' or 'eu'
user_id = "user:<user_name>"
schemaId = ""


def startMenu():
    print("starting menu and setting up env")
    setup()
    while True:
        user_input = int(input("Enter the API number according to \n"
                               "1. Get SchemaList\n"
                               "2. Get SchemaById\n"
                               "3. create Schema\n"
                               "4. update Schema \n"
                               "5. Delete Schema \n"
                               "6. Create Document \n"
                               "7. Get Document By Id\n"
                               "8. Get Document By RefId\n"
                               "9. Delete Document By Id\n"
                               "10. Delete Document By RefId \n"
                               "11. Update Document By Id\n"
                               "12. Update Document By RefId \n"
                               "13. Search Docuemnts \n"
                               "14. Create Folder  \n"
                               "15. Create Folder Object By Folder SchemaId\n"
                               "16. Link Document To Folder\n"
                               "17. List Documents Under Folder \n"
                               "18. Remove Document from a folder with link Id \nEnter Value here ::: "))
        if user_input == 0:
            break
        switch_cases = {
            1: getSchemaList,
            2: getSchemaById,
            3: createSchema,
            4: updateSchema,
            5: deleteSchema,
            6: createDocument,
            7: getDocumentById,
            8: getDocumentByRefId,
            9: deleteDocumentById,
            10: deleteDocumentByRefId,
            11: updateDocumentById,
            12: updateDocumentByRefId,
            13: search,
            14: createFolder,
            15: createFolderObjectByFolderSchemaId,
            16: linkDocumentToFolder,
            17: listDocumentsUnderFolder,
            18: removeDocumentFromFolderWithLinkId
        }

        method = switch_cases.get(user_input)
        print("printing method val:: ", method)
        if method is not None:
            method()
        else:
            print("Invalid input.")


def setup():
    os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"] = "<ADC Path>"


def getSchemaList():
    response = GetSchemaList.sample_list_document_schemas(project_number, location)
    print(response)


def getSchemaById():
    schemaId = str(input("Enter schemaId : "))
    response = GetSchemaById.get_document_schema_by_id(project_number, location, schemaId)
    print(response)

def createSchema():
    schemaId = str(input("Enter schemaId : "))
    response = CreateSchema.createSchema(project_number, location, user_id)
    print(response)

def updateSchema():
    schemaId = str(input("Enter schemaId : "))
    response = UpdateSchema.update_document_schema(project_number, location, schemaId)
    print(response)

def deleteSchema():
    schemaId = str(input("Enter schemaId : "))
    response = DeleteSchema.sample_delete_document_schema(project_number, location, schemaId)
    print(response)

def createDocument():
    schemaId = str(input("Enter schemaId : "))
    response = CreateDocument.createDocument(project_number, location, user_id, schemaId)
    print(response)

def getDocumentById():
    docuemntId = str(input("Enter documentId : "))
    response = GetDocument.getDocumentById(project_number,location,user_id,docuemntId)
    print(response)

def getDocumentByRefId():
    docuemntRefId = str(input("Enter document reference Id : "))
    response = GetDocument.getDocumentByRefId(project_number,location,user_id,docuemntRefId)
    print(response)

def updateDocumentById():
    docuemntId = str(input("Enter documentId : "))
    schemaId = str(input("Enter schemaId : "))
    response = UpdateDocument.updateDocumentById(project_number,location,user_id,docuemntId,schemaId)
    print(response)

def updateDocumentByRefId():
    docuemntRefId = str(input("Enter document reference Id : "))
    response = UpdateDocument.updateDocumentByRefId(project_number,location,user_id,docuemntRefId)
    print(response)

def deleteDocumentById():
    documentId = str(input("Enter documentId : "))
    response = DeleteDocument.deleteDocumentById(project_number, location, user_id, documentId)
    print(response)

def deleteDocumentByRefId():
    docuemntRefId = str(input("Enter document reference Id : "))
    response = DeleteDocument.deleteDocumentByRefId(project_number,location,user_id,docuemntRefId)
    print(response)

def search():
    query = str(input("Enter search query val : "))
    response = Search.search(project_number,location,user_id,query)
    print(response)

def createFolder():
    FolderName = str(input("Enter folder name : "))
    response = CreateFolder.create_folder_schema(project_number,location,FolderName)
    print(response)

def createFolderObjectByFolderSchemaId():
    FolderShemaName = str(input("Enter folder schema : "))
    response = CreateFolderObjectByFolderSchemaId.createFolderObejectByFolderSchemaId(project_number,location,user_id,FolderShemaName)
    print(response)

def linkDocumentToFolder():
    FolderId = str(input("Enter folder Id : "))
    docuemntid = str(input("Enter Document Id : "))
    response = AddDocumentToFolder.add_to_folder(project_number , location, user_id ,FolderId , docuemntid)
    print(response)

def listDocumentsUnderFolder():
    FolderId = str(input("Enter folder Id : "))
    response = ListDocumentUnderFolder.list_sub_docs(project_number , location, user_id ,FolderId)
    print(response)

def removeDocumentFromFolderWithLinkId():
    FolderId = str(input("Enter folder Id : "))
    linkId = str(input("Enter link Id : "))
    response = RemoveDocumentFromFolder.remove_doc_from_folder_with_link_id(project_number , location, user_id,FolderId ,linkId)
    print(response)


startMenu()