# mohammed97ashraf/ApplyWizard

⭐ 15 · Python · MIT · 推送 2026-06-13 · [GitHub](https://github.com/mohammed97ashraf/ApplyWizard) · 个人维护

**用 LangChain ReAct Agent 与 AgentQL 自动填写求职申请表单的工具**

面向求职者的 Python 工具：结合 LangChain、ReAct Agent 与 AgentQL，读取网页中的申请表单并自动填写，替代重复性的手工投递操作。运行需 OpenAI API key 与 AgentQL API key，LangChain key 仅用于可选的追踪；通过 git clone 源码安装并 pip 安装依赖，用户自建 run.py 脚本调用 AgentExecutor 运行。文档文件夹标注 coming soon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 LangChain openai_tools_agent 的 AgentExecutor 示例运行方式
- AgentQL 用于网页表单识别与交互
- 支持 .env 配置 API key，LangChain tracing 为可选项

## 适用场景

- 投递岗位时自动填写重复的申请表单
- 定制自己的求职申请自动化脚本

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Automate your job application process with AI-powered form filling using **LangChain**, **ReAct Agent**, and **Agent
> L8: - **Automate**: Let AI fill out your job applications.

## 星数曲线

```mermaid
xychart-beta
    title "mohammed97ashraf/ApplyWizard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `2477a491dacb` · [字段定义](../../DATASET.md)*
