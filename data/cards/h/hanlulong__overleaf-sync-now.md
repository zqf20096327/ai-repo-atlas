# hanlulong/overleaf-sync-now

⭐ 18 · Python · MIT · 推送 2026-05-30 · [GitHub](https://github.com/hanlulong/overleaf-sync-now) · [官网](https://openecon.ai/) · 个人维护

**防止 Claude Code/Codex 用过期本地副本覆盖 Overleaf 网页编辑的同步钩子**

面向使用 Overleaf Premium Dropbox 同步并配合 Claude Code / Codex CLI 本地编辑 .tex 的作者：Overleaf 向 Dropbox 推送网页编辑有 10–20 分钟轮询延迟，AI 读到过期文件并写回会静默覆盖网页新编辑。该工具以 Claude Code PreToolUse 钩子、CLI 与 agent skill 形式提供，在每次 AI 读写 .tex/.bib 等文件前探测 Overleaf 版本历史（/project/<id>/updates），存在网页来源更新时下载 zip 并仅写入变更文件，保留 Dropbox 设置不变；含 30 秒防抖与不覆盖 30 秒内本地修改的安全保护。Python 3.8+，经 uv 工具从 git 安装，Windows Chrome 130+ 需额外运行 login 命令完成认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PreToolUse 钩子在每次 AI 读写 .tex/.bib 等文件前自动触发同步
- 版本匹配探测：无变化时约 0.3–1 秒只读探测，有更新才下载 zip 并按哈希比对写入
- 自动把 Dropbox Apps/Overleaf 目录映射到 Overleaf 项目 ID，重名项目时列出候选让用户选择
- 数据安全保护：不覆盖 30 秒内被本地修改的文件，每项目 30 秒防抖

## 适用场景

- 多设备在 overleaf.com 网页与本地交替编辑论文时，防止 AI 覆盖网页端新改动
- 保留 Dropbox 免费多设备同步机制的同时让 AI 编辑前拿到最新版本
- 协作写作场景下保证本地 AI 编辑不回滚协作者的网页修改

## 场景标签

 · 领域:学术写作/开发者工具

## 证据(README 行号)

> L14: `overleaf-sync-now` is an **agent skill** (plus a CLI and a Claude Code PreToolUse hook) that closes this gap. Befo
> L83: 1. The **PreToolUse hook** intercepts every `Read` / `Edit` / `Write` / `MultiEdit` of `.tex` / `.bib` / `.cls` / `

## 星数曲线

```mermaid
xychart-beta
    title "hanlulong/overleaf-sync-now 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f607842e38e7` · [字段定义](../../DATASET.md)*
