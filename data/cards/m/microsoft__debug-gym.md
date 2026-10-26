# microsoft/debug-gym

⭐ 308 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/microsoft/debug-gym) · [官网](https://aka.ms/debug-gym/) · 组织维护

**供 LLM agent 交互式调试 Python 代码的文本环境框架**

微软开源的文本交互式调试框架：以 Gymnasium 范式提供仿真环境，agent 可通过 pdb、bash、view、edit、grep 等工具迭代探索代码仓库并提出补丁，环境执行测试用例返回结果；附带 LLM 后端抽象（OpenAI、Azure OpenAI、Hugging Face/vLLM、Anthropic）、示例 agent 与 swebench/aider/r2egym 等基准集成，终端后端支持 Docker 与 Kubernetes。要求 Python>=3.12，非 Linux 平台对 pdb 工具支持有限。面向构建与评测调试 agent 的开发者/科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gymnasium 范式的交互式调试环境（reset/step）
- bash/pdb/edit/grep 等 9 类可动态加载的工具，支持 MCP 外部工具注册
- 支持 OpenAI、Azure OpenAI、Hugging Face/vLLM、Anthropic 后端
- Docker 与 Kubernetes 两种终端后端，内置多级超时机制

## 适用场景

- 构建和评测 LLM 驱动的自动调试 agent
- 在 SWE-bench 等基准上复现调试实验
- 开发自定义调试工具并接入 agent 动作空间

## 场景标签

`编码 Agent` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L69: `debug_gym.gym` is a simulation environment. Given a code repository, an agent can iteratively interact with a set 
> L73: `debug_gym.llms` are the different LLM backends that can be used to instantiate agents. Currently, we support OpenA

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/debug-gym 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 307 --> 309
    line [308, 308]
```

2026-10-18 308 → 2026-10-26 308（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `905759026c2e` · [字段定义](../../DATASET.md)*
