# wupd1122/llama2.c-260k-rtl-fpga

⭐ 23 · Verilog · 推送 2026-05-30 · [GitHub](https://github.com/wupd1122/llama2.c-260k-rtl-fpga) · 个人维护

**在 FPGA 上用 Verilog RTL 实现 llama2.c stories260K 前向推理**

工程实践项目：将开源 llama2.c 的 stories260K 模型逐步映射为 Verilog RTL，完成从基础算子、向量模块、Transformer 子模块、单层、5 层前向核心到 UART 顶层 token 推理的 6 级开发路径。PC 侧负责分词与解码，FPGA 侧执行 embedding、Transformer 前向、分类器与 argmax，通过 UART 交互实现 token_id 到 next_token_id 的最小推理链。附带 cocotb 仿真、Vivado 工程（目标器件 XCVU9P-2FLGB2104I）与可用的 bitstream。限制：模型与参数包固定于 stories260K，非通用推理框架，板级工程绑定当前验证平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 级开发路径：基础算子到 UART 顶层 token 推理全部完成
- PC/FPGA 分工：PC 分词与解码，FPGA 前向与 argmax
- 每级提供 RTL、cocotb testbench 与仿真入口脚本
- 保留最终 Vivado 工程与可直接烧写的 bitstream（XCVU9P-2FLGB2104I）

## 适用场景

- 学习 Transformer 前向的 RTL 实现与仿真验证流程
- 在 XCVU9P 板卡上复现 stories260K 的 UART token 推理
- 研究小型语言模型在 FPGA 上的部署与资源占用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: `llama2.c-260k-rtl-fpga` is an engineering project that progressively maps the `stories260K` model from the open-sou
> L23: token_id -> FPGA forward -> next_token_id

## 星数曲线

```mermaid
xychart-beta
    title "wupd1122/llama2.c-260k-rtl-fpga 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f13dae416146` · [字段定义](../../DATASET.md)*
