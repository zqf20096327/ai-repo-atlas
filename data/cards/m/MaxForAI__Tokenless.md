# MaxForAI/Tokenless

⭐ 46 · JavaScript · MIT · 推送 2026-05-19 · [GitHub](https://github.com/MaxForAI/Tokenless) · 组织维护 · 中文 README

**为 Claude Code 减少 token 用量的上下文压缩钩子工具**

通过 Claude Code hooks 拦截大体积工具输出：将测试/构建日志、diff、搜索与大文件读取的原始内容存为本地 artifact，向模型发送紧凑的 TOKENLESS-* 摘要包，需要时可按行号展开原文；提供 chat/coding/off 三种输出风格，launcher 默认禁用 Task/Plan 等高开销工具；edit/write 包策略保守，失败或风险输出不做压缩。附 API-body 实测基准与外部研究引文。经 GitHub 以 npm 全局安装，未发布到公共 npm registry。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将大输出/大读取压缩为 TOKENLESS-* 包，原文存本地 artifact 可按行展开
- 三种输出风格 chat/coding/off，风格配置跨会话持久化
- launcher 默认禁用 TaskCreate/EnterPlanMode 等高开销工具，可用环境变量恢复
- 附 API-body 实测基准（请求 token 最高降 80%）与研究引文

## 适用场景

- 降低 Claude Code 长会话的 API token 消耗
- 让 vibe coding 会话中的测试日志、diff、大文件读取不再反复占用上下文
- 通过 /tokenless 斜杠命令查看节省统计与包状态

## 场景标签

 · 领域:LLM 基础设施/上下文管理

## 证据(README 行号)

> L179:   -> Tokenless intercepts it with Claude Code hooks
> L182:   -> Claude receives a compact TOKENLESS-* packet
> L273: `tokenless launch` starts Claude Code with normal read, edit, write, and bash tools available, but disables high-o

## 星数曲线

```mermaid
xychart-beta
    title "MaxForAI/Tokenless 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `0ad5ebc9ec57` · [字段定义](../../DATASET.md)*
