# LangGraph-GUI/CrewAI-GUI-Qt

⭐ 210 · Python · MIT · 推送 2026-07-14 · [GitHub](https://github.com/LangGraph-GUI/CrewAI-GUI-Qt) · [官网](https://langgraph-gui.github.io/CrewAI-GUI-Qt/) · 组织维护

**CrewAI 的节点式图形前端：拖拽设计 AI 工作流**

基于 PySide6 的 CrewAI 前端：通过拖拽节点界面设计 AI agent 交互的 DAG 结构，保存/加载为 JSON 文件；后端读取 JSON 并转换为 CrewAI 任务与 agent 执行，支持 GPT-4 API 与 Ollama 两种后端。跨 Windows/Linux/macOS，可用 PyInstaller 打包为独立可执行文件。当前版本仅支持有限的节点类型和槽位，部分高级 CrewAI 特性尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 拖拽式节点界面设计 agent DAG，导出/导入 JSON
- 后端将 JSON 转换为 CrewAI 任务与 agent 运行
- 支持 GPT-4 API 与 Ollama 后端
- PyInstaller/cx_Freeze 打包为独立可执行文件

## 适用场景

- 用图形界面设计 CrewAI 多 agent 工作流
- 将 agent 工作流以 JSON 保存、复用与分享
- 配合本地 Ollama 模型运行设计的 agent 流程

## 场景标签

`多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L3: *A Node-Based Frontend for CrewAI: Revolutionizing AI Workflow Creation*
> L74: The backend seamlessly converts JSON files into CrewAI tasks and agents.

## 星数曲线

```mermaid
xychart-beta
    title "LangGraph-GUI/CrewAI-GUI-Qt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 209 --> 211
    line [210, 210]
```

2026-10-18 210 → 2026-10-22 210（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `41a429dfdaa1` · [字段定义](../../DATASET.md)*
