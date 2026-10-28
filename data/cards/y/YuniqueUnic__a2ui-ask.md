# YuniqueUnic/a2ui-ask

⭐ 27 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/YuniqueUnic/a2ui-ask) · [官网](https://yuniqueunic.github.io/schemaui/) · 个人维护 · 中文 README

**把 AI agent 的结构化提问转成浏览器表单的技能**

面向 Claude Code、Codex、Cursor 等 agent 的技能（skill）：当 agent 需要用户做选择或填写结构化配置时，调用本地脚本生成基于 schema 的浏览器表单（schemaui 引擎，绑定 0.0.0.0，可从手机/SSH 隧道访问），支持校验、默认值、多选、滑块、条件字段与 Mermaid 图表等控件；答案持久化为带时间戳的 JSON 文件形成审计记录。安装需先装 schemaui 二进制（自动安装脚本支持 GitHub/Gitee 双源），再以 npx skills add、agent 代装或手动 clone 三种方式装技能。

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

- 由 JSON schema 生成带校验与多选的浏览器表单，替代终端问答
- 答案持久化到 .schemaui/answers/ 形成决策审计记录
- 控件覆盖滑块、分段控件、取色器、条件字段及 Mermaid 实时预览编辑器
- 安装脚本支持 Gitee 镜像回退，可指定 --source github|gitee

## 适用场景

- 让 coding agent 在无 TTY 的子进程中向我收集部署配置
- 通过手机或 SSH 隧道远程回答 agent 提出的结构化问题
- 保留每次决策的 JSON 答案记录供事后审计

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: Give your AI agent a real UI. When Claude Code, Codex, Cursor, or any other
> L43: 1. **Browser form, not terminal.** The agent spawns a local Web UI
> L86: npx skills add YuniqueUnic/a2ui-ask

## 星数曲线

```mermaid
xychart-beta
    title "YuniqueUnic/a2ui-ask 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-28 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6ca688ab4147` · [字段定义](../../DATASET.md)*
