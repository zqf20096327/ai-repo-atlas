# Tian-ye1214/RedLotus

⭐ 42 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/Tian-ye1214/RedLotus) · 个人维护 · 中文 README

**终端多 Agent AI 助手：任务编排、长期记忆与运行时技能**

基于 Pydantic AI 构建的终端 AI Agent：Coordinator 根据请求复杂度选择直接执行、委派单个 Worker 或由 Manager 拆解协调复杂任务，支持 OpenAI 兼容模型 API。提供三层记忆（会话记录、项目情节、全局长期 RAG）、运行时 SKILL.md 技能、文件与媒体提取（PDF/Word/Excel 等）、全屏 TUI 的 diff 审查与路径沙箱等安全机制。可选浏览器自动化、本地语音识别/合成、QQ/微信机器人与桌面宠物。需 Python 3.12+，支持 Windows/Linux/macOS，另提供 Windows x64 可执行文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Coordinator/Manager/Worker 多 Agent 编排，依赖感知分批执行
- 三层记忆与 MEMORY.md 核心画像，运行时自动重扫 SKILL.md 技能
- 上下文容量拒绝时按完整证据边界拆分并发压缩后重试
- 路径沙箱、危险命令拦截、子进程清理等运行时安全机制

## 适用场景

- 在终端用自然语言完成需要多步工具调用的复杂任务
- 让 Agent 围绕目标持续迭代直到完成
- 通过 QQ/微信机器人或桌面宠物与 Agent 交互

## 场景标签

`AI 助手` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A terminal AI agent with task orchestration, long-term memory, and runtime skills.
> L12: RedLotus is an AI agent that runs in your terminal. It chooses how to handle each request based on its complexity: 

## 星数曲线

```mermaid
xychart-beta
    title "Tian-ye1214/RedLotus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-29 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c01105bd8fc3` · [字段定义](../../DATASET.md)*
