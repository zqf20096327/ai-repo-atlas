# angrysky56/mcp-logic

⭐ 47 · Python · MIT · 推送 2026-08-15 · [GitHub](https://github.com/angrysky56/mcp-logic) · 个人维护

**一阶逻辑推理 MCP 服务器：为 AI 客户端提供定理证明与模型求解工具**

基于 Model Context Protocol 的逻辑推理服务器：封装 Prover9 定理证明、Mace4 有限模型查找与反例生成、语法校验、范畴论推理、HCC 命题判定与 VFE 溯因推理共 9 个工具。可选的 Logic Advisor 使用本地 TwIL-LM3 3B 模型（Q8_0 GGUF，约 3.3GB，经 llama-cpp-python 加载）将英文问题转译为一阶逻辑并解释求解结果，支持 CUDA/Metal/CPU，模型许可为非商业。支持 Claude Desktop 与 Codex 接入，提供 Linux/Windows 一键安装脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Prover9 定理证明与 Mace4 模型查找/反例生成
- 9 个 MCP 工具：证明、语法校验、范畴论交换律验证、HCC 命题判定、VFE 溯因等
- 可选 TwIL-LM3 本地 3B 顾问 LLM：英文提问→形式化→求解→解释
- 自动检测 CUDA/Metal/CPU 并编译 llama-cpp-python

## 适用场景

- 在 Claude Desktop 或 Codex 中调用定理证明与反例查找工具
- 用自然语言提问并由本地 LLM 顾问形式化并求解逻辑问题
- 范畴论公理获取与图的交换律验证

## 场景标签

 · 领域:AI 工具/形式逻辑

## 证据(README 行号)

> L5: An MCP server for automated first-order logic reasoning using Prover9, Mace4, and an onboard reasoning LLM.
> L246: │   ├── server.py              # Main MCP server (9 tools)

## 星数曲线

```mermaid
xychart-beta
    title "angrysky56/mcp-logic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-29 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `284a18505f2d` · [字段定义](../../DATASET.md)*
