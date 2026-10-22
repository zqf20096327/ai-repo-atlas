# nekocode/filetree-skill

⭐ 162 · Python · 推送 2026-07-20 · [GitHub](https://github.com/nekocode/filetree-skill) · [官网](https://nekocode.github.io/filetree-skill/) · 个人维护 · 中文 README

**Claude Code 插件：用 FILETREE.md 维护文件级索引供 LLM 快速理解仓库**

面向 Claude Code 的插件，生成并维护 FILETREE.md：每个文件一行职责描述，内容哈希存于旁车文件用于漂移检测，LLM 读几百 token 即可掌握仓库布局。提供 init/update/lint/uninstall 四条命令，lint 为只读检查不调用 LLM，可在 CI 使用。变更检测依赖 git，零后台进程，Python 标准库实现。支持将索引挂接进 CLAUDE.md/AGENTS.md，以及不提交产物的 self-only 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每文件一行描述 + 旁车内容哈希做漂移检测
- UNCHANGED 策略：职责未变时仅刷新哈希以降低 token 消耗
- /filetree:lint 只读检查、不调用 LLM、CI 友好
- self-only 模式经 .git/info/exclude 隐藏全部产物

## 适用场景

- 让 Claude Code 会话免于反复 ls/grep 重新探索仓库结构
- 把仓库布局索引提交 git 与协作者共享
- 在 CI 中检测 FILETREE.md 与实际代码的漂移

## 场景标签

 · 领域:AI 编码工具/开发者效率

## 证据(README 行号)

> L5: A Claude Code plugin that maintains `FILETREE.md` — a one-line description per file with content hashes for stalenes
> L128: |Claude Code|any|Plugin format. `claude` is shipped as a native binary; Node is not required|
> L126: |`git`|any modern release|Required at runtime; non-git repos fail fast with a clear error|
> L127: |`python3`|≥ 3.9|Uses PEP 585 `list[dict]` builtin generics. Stdlib only — zero third-party deps. The plugin invok

## 星数曲线

```mermaid
xychart-beta
    title "nekocode/filetree-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 161 --> 163
    line [162, 162]
```

2026-10-18 162 → 2026-10-22 162（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6a093682a9e3` · [字段定义](../../DATASET.md)*
