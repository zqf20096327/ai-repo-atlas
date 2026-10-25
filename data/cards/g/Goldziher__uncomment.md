# Goldziher/uncomment

⭐ 140 · Rust · MIT · 推送 2026-10-19 · [GitHub](https://github.com/Goldziher/uncomment) · 个人维护

**基于 tree-sitter AST 移除代码注释并做 TODO 类注释 lint 的 CLI**

Rust 编写的命令行工具，用 tree-sitter 将代码解析为语法树后仅对真实注释节点操作：删除注释（默认保留 TODO/FIXME、文档注释与 lint 指令），并可对 TODO/FIXME/HACK/XXX 做 lint 检查是否携带 issue key，支持 --check 在提交或 PR 门禁中使用，可按整棵树、分支变更或暂存区限定范围。支持 306 种语言（55 种内置配置），语法已编译进二进制，运行时无需下载。README 提及最初为清理 AI 生成代码中的解释性注释而开发，但工具本身不调用任何模型。提供 Homebrew、cargo、npm、pip 安装与预编译二进制，macOS/Linux/CI 可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- tree-sitter AST 解析，不误删字符串内类注释文本
- 306 种语言支持（55 种内置配置），语法编译进二进制
- uncomment lint 检查 TODO/FIXME/HACK/XXX 是否携带真实 issue key
- scan 子命令输出全库注释清单（JSONL/JSON/text）

## 适用场景

- 清理 AI 生成代码中大量解释性注释
- 在 CI 中以 --check 门禁禁止残留 TODO 或违规注释
- 统计代码库注释清单并按删除/保留分类

## 场景标签

 · 领域:开发者工具/代码处理

## 证据(README 行号)

> L5: uncomment is a comment remover and a comment linter, both built on tree-sitter's AST — so both are
> L29: Originally built to clean up AI-generated code drowning in explanatory comments, it now works on
> L43: - **306 languages** — powered by tree-sitter-language-pack, every grammar compiled into the binary

## 星数曲线

```mermaid
xychart-beta
    title "Goldziher/uncomment 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 134 --> 140
    line [135, 139, 139]
```

2026-10-18 135 → 2026-10-25 139（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3c2634e51110` · [字段定义](../../DATASET.md)*
