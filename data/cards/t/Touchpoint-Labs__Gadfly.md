# Touchpoint-Labs/Gadfly

⭐ 48 · Python · MIT · 推送 2026-07-15 · [GitHub](https://github.com/Touchpoint-Labs/Gadfly) · 组织维护

**AI 编码 agent 的监督层：工具调用前拦截漂移与缺陷**

嵌入 Claude Code 工具调用循环（PreToolUse）的监督工具：在每次动作执行前由两个独立只读 LLM 审查者（Architect 默认 Opus、Code Reviewer 默认 Sonnet）做出 allow/question/surface/block 四种裁决，确定性首过自动放行读取与安全命令。以分层记忆文件（spec.md/claude.md/codemap.md 等）为依据执行规格，带自主度三档、编辑台账与空闲时偏好规则提取。v1 仅支持 Claude Code，运行于其订阅之上或改用 Anthropic API。pip 安装，零依赖，Python 3.11+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PreToolUse 钩子在每个工具调用前做四档裁决（allow/question/surface/block）
- 双独立监督者：Architect（规格/漂移）与 Code Reviewer（逻辑缺陷）
- 分层记忆（spec.md 等）驱动规格绑定，agent 不可写关键文件
- 从用户带外编辑中提取持久化偏好规则，空闲时执行

## 适用场景

- 让 AI 编码 agent 长时间自主工作而无需逐步审批
- 在代码执行前拦截与规格漂移或真实缺陷
- 把项目规格变为被持续执行而非搁置的文档

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L14: Gadfly sits inside your coding agent's live tool-call loop and does what Socrates did to
> L52: At every tool call, **before it executes** (`PreToolUse`), Gadfly reviews the action with
> L151: In v1, Gadfly supervises only Claude Code, so you'll need it installed first. Then:

## 星数曲线

```mermaid
xychart-beta
    title "Touchpoint-Labs/Gadfly 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 46 --> 49
    line [47, 48, 48]
```

2026-10-18 47 → 2026-10-30 48（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8fb6cd5b014c` · [字段定义](../../DATASET.md)*
