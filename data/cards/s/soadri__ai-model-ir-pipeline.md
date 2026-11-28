# soadri/ai-model-ir-pipeline

⭐ 3 · Rust · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/soadri/ai-model-ir-pipeline) · [官网](https://soadri.github.io/ai-model-ir-pipeline/) · 组织维护

**将 PyTorch 模型 lowering 到 NPU IR 并在模拟器上验证的转换流水线**

面向 AI 模型编译的开发者工具：通过 torch-mlir 将 PyTorch 模型转为标准 MLIR（linalg），分析运算模式后 lowering 为 NPU 专属 IR（RNGD Dialect），并按三个层级验证——IR 结构一致性、运算转换覆盖、模拟器执行结果与 PyTorch 基准的数值误差。提供 Web 仪表盘与 CLI，输出转换规则注册表、转换覆盖报告与 IR/内核源码。验证针对 Llama 系 Decoder Layer 结构，reduce 独立运算走 CPU fallback，torch-mlir 版本固定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch→标准 MLIR(linalg)→NPU 专属 IR 的分层转换流水线
- 三级验证：IR 一致性 12 项 + 模拟器数值比对
- 26 条转换规则注册表，经仪表盘与 API 公开
- 用户自定义 nn.Module 的转换覆盖与未支持运算分析

## 适用场景

- 查看我的 PyTorch 模型逐算子 lowering 到 NPU IR 的过程
- 检查自定义模型有哪些算子暂不支持转换
- 在 NPU 模拟器上比对转换后算子与 PyTorch 的数值结果

## 场景标签

 · 领域:AI 基础设施/模型编译

## 证据(README 行号)

> L12: AI 모델 변환(표준 IR) 파이프라인은 PyTorch로 작성된 AI 모델이 NPU에서 실행 가능한 형태로 바뀌는 과정을 단계별로 보여주고 검증하는 오픈소스 도구입니다. 모델을 표준 MLIR(linalg) 
> L25: PyTorch 모델은 torch-mlir을 통해 표준 MLIR의 linalg 연산으로 변환되고(1\~3), 파이프라인이 이 연산들을 분석해 NPU 특화 IR 연산으로 바꿉니다(4). 이후 연산별 커널을 구성
> L74: Docker만 있으면 됩니다. 이미지(내려받기 약 380MB)는 GitHub Container Registry에서 받습니다.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `ec7a787def08` · [字段定义](../../DATASET.md)*
