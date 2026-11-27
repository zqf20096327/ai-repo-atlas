# sadrjahani/react-agent-from-scratch

⭐ 4 · Python · MIT · 推送 2026-11-06 · [GitHub](https://github.com/sadrjahani/react-agent-from-scratch) · [官网](https://sadrjahani.github.io) · 个人维护

**Python 实现的 ReAct 工具调用 Agent 教学项目**

不依赖 agent 框架、从零实现的 ReAct 循环：LLM 选择工具、接收 Observation、迭代至给出最终答案或达到迭代上限。实现按模块拆分为 prompt 构造、响应解析、模型访问、工具执行与编排；通过 provider 无关的 chat() 接口支持 Ollama 与 OpenAI 后端。内置计算器、离线事实查找、限定 data/ 目录的文件读取三个工具，带 CLI、确定性测试套件与可配置迭代上限。README 明确其评估集非代表性基准，文件工具也非加固沙箱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- provider 无关的 chat() 接口，默认本地 Ollama，可切换 OpenAI
- 编排循环记录每次 LLM 调用时长并强制迭代上限，工具错误回传为 Observation
- 计算器用 AST 白名单求值而非 eval()，文件读取限定 data/ 目录
- 确定性测试套件不依赖在线模型或 API 凭据

## 适用场景

- 本地用 Ollama 运行一个可调用工具的 ReAct Agent
- 学习 ReAct 循环的模块化实现与解析/错误恢复机制
- 以注入假 LLM 的方式做 Agent 逻辑的自动化测试

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A compact **ReAct (Reason + Act) agent implemented in Python**, without an agent framework. A language model can sel
> L15: - A provider-independent `chat()` interface for supported Ollama and OpenAI configurations.
> L23: - **Explicit orchestration:** The control loop is implemented in the repository rather than delegated to an agent f

## 星数曲线

```mermaid
xychart-beta
    title "sadrjahani/react-agent-from-scratch 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-27"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-08 4 → 2026-11-27 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `5e966ddc97ee` · [字段定义](../../DATASET.md)*
