# Scottcjn/rpi-inference

⭐ 40 · C · AGPL-3.0 · 推送 2026-08-06 · [GitHub](https://github.com/Scottcjn/rpi-inference) · [官网](https://rustchain.org) · 个人维护

**零乘法文本生成引擎：用置换表查表替代矩阵乘法，可做LLM投机草稿**

面向极端硬件受限环境的推理引擎：用置换指令（vec_perm/vperm/tbl）与整数累加替代浮点矩阵乘法，模型 0.3-3 MB，支持 POWER8、G4/G5、x86（含386+）、ARM、MIPS（N64）等平台。提供 C 引擎（make 构建）与 Python 原型工具，可从教师 LLM 蒸馏生成 .rpi 模型。支持三种与 LLM 协作模式：投机草稿引擎、输入分类路由、混合生成。限制：N64 与 Pi5 吞吐部分为估计值或待实测，RISC-V/SPARC 后端为 planned。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 置换表查表替代矩阵乘法，整条流水线零乘法、无浮点
- 模型 0.3-3 MB，Python 端 18,000 tok/s、POWER8 C 端 84+ tok/s
- 支持 POWER8/PowerPC G4-G5/x86/AArch64/ARM32/MIPS 等平台
- 可从教师 LLM 的实际生成分布蒸馏出转移表构建模型

## 适用场景

- 在无 GPU 的老旧或嵌入式 CPU（含 N64、树莓派）上运行文本生成
- 作为 LLM 的投机解码草稿引擎降低推理开销
- 对入站请求做微秒级分类路由到不同专用 LLM

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: **Zero-multiply inference engine. Table-driven. Cache-resonant. Hardware-timed.**
> L9: RPI replaces matrix multiplication with permutation table lookups and integer accumulation. No floating point. No GE
> L55: python3 tools/distill_to_rpi.py --teacher tinyllama --output sophia.rpi


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `01637a571d86` · [字段定义](../../DATASET.md)*
