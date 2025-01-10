"""
Module containing tools for generating cross-client Ethereum execution layer
tests.
"""

from ethereum_test_base_types import (
    AccessList,
    Account,
    Address,
    Bytes,
    Hash,
    TestAddress,
    TestAddress2,
    TestPrivateKey,
    TestPrivateKey2,
)
from ethereum_test_base_types.reference_spec import ReferenceSpec, ReferenceSpecTypes
from ethereum_test_exceptions import (
    BlockException,
    EngineAPIError,
    EOFException,
    TransactionException,
)
from ethereum_test_fixtures import BaseFixture, FixtureCollector, TestInfo
from ethereum_test_specs import (
    SPEC_TYPES,
    BaseTest,
    BlockchainTest,
    BlockchainTestEngine,
    BlockchainTestEngineFiller,
    BlockchainTestFiller,
    EOFStateTest,
    EOFStateTestFiller,
    EOFTest,
    EOFTestFiller,
    StateTest,
    StateTestFiller,
    TransactionTest,
    TransactionTestFiller,
)
from ethereum_test_specs.blockchain import Block, Header
from ethereum_test_types import (
    EOA,
    Alloc,
    AuthorizationTuple,
    ConsolidationRequest,
    DepositRequest,
    Environment,
    Removable,
    Requests,
    Storage,
    TestParameterGroup,
    Transaction,
    Withdrawal,
    WithdrawalRequest,
    add_kzg_version,
    ceiling_division,
    compute_create2_address,
    compute_create_address,
    compute_eofcreate_address,
    keccak256,
)
from ethereum_test_vm import (
    Bytecode,
    EVMCodeType,
    Macro,
    Macros,
    Opcode,
    OpcodeCallArg,
    Opcodes,
    UndefinedOpcodes,
    call_return_code,
)

from .code import (
    CalldataCase,
    Case,
    CodeGasMeasure,
    Conditional,
    Initcode,
    Switch,
    Yul,
    YulCompiler,
)
from .utility.generators import DeploymentTestType, generate_system_contract_deploy_test
from .utility.pytest import extend_with_defaults

__all__ = (
    "SPEC_TYPES",
    "AccessList",
    "Account",
    "Address",
    "Alloc",
    "AuthorizationTuple",
    "BaseFixture",
    "BaseTest",
    "Block",
    "BlockchainTest",
    "BlockchainTestEngine",
    "BlockchainTestEngineFiller",
    "BlockchainTestFiller",
    "BlockException",
    "Bytecode",
    "Bytes",
    "CalldataCase",
    "Case",
    "CodeGasMeasure",
    "Conditional",
    "ConsolidationRequest",
    "DepositRequest",
    "DeploymentTestType",
    "EngineAPIError",
    "Environment",
    "EOFException",
    "EOFStateTest",
    "EOFStateTestFiller",
    "EOFTest",
    "EOFTestFiller",
    "EVMCodeType",
    "FixtureCollector",
    "Hash",
    "Header",
    "Initcode",
    "Macro",
    "Macros",
    "Opcode",
    "OpcodeCallArg",
    "Opcodes",
    "UndefinedOpcodes",
    "ReferenceSpec",
    "ReferenceSpecTypes",
    "Removable",
    "Requests",
    "EOA",
    "StateTest",
    "StateTestFiller",
    "Storage",
    "Switch",
    "TestAddress",
    "TestAddress2",
    "TestInfo",
    "TestParameterGroup",
    "TestPrivateKey",
    "TestPrivateKey2",
    "Transaction",
    "TransactionException",
    "TransactionTest",
    "TransactionTestFiller",
    "Withdrawal",
    "WithdrawalRequest",
    "Yul",
    "YulCompiler",
    "add_kzg_version",
    "call_return_code",
    "ceiling_division",
    "compute_create_address",
    "compute_create2_address",
    "compute_eofcreate_address",
    "extend_with_defaults",
    "generate_system_contract_deploy_test",
    "keccak256",
    "vm",
)
