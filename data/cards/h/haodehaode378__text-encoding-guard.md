# haodehaode378/text-encoding-guard

⭐ 44 · Python · MIT · 推送 2026-07-16 · [GitHub](https://github.com/haodehaode378/text-encoding-guard) · [官网](https://github.com/haodehaode378/text-encoding-guard) · 个人维护 · 中文 README

**检测并修复 AI 编码助手造成的中文乱码的工具**

针对 AI 编码助手编辑含中文文件时产生的 UTF-8/GBK 编码损坏，提供评分制检测（口字码、破标签、锟拷码等七大维度，总分>0 即标记）与保守修复（--fix-gbk 遵循三重安全门，GB18030/UTF-8 双向尝试，修复前备份）。纯 Python stdlib，零依赖，默认扫描 20 种扩展名。面向使用 Claude Code、Cursor、Copilot 等助手的开发者，支持 GitHub Action（PR 拦截、退出码 2）与 Claude Code PostToolUse hook 编辑后自动触发，另有可选 skill 安装。限制：主要覆盖中英文编码损坏场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七大维度评分制乱码检测（替换字符、破标签、锟斤拷等）
- --fix-gbk 三重安全门双向修复（UTF-8↔GBK/GB18030）
- GitHub Action 一行集成，PR 含乱码自动拦截
- Claude Code PostToolUse hook 每次编辑后自动检测
- 零依赖，纯 Python stdlib

## 适用场景

- AI 编码助手改完中文文件后自动检查是否产生乱码
- 在 CI 中拦截含乱码的 PR 合入
- 批量扫描并修复项目中已有的乱码文件

## 场景标签

 · 领域:开发者工具/代码质量

## 证据(README 行号)

> L14: **AI 编码助手把中文搞成乱码了？自动检测，一键修复。**
> L20: 当 AI 编码助手（Claude、Cursor、Copilot、Codex）编辑含中文的文件时，编码损坏会悄然发生。UTF-8 字节被误读为 GBK — 等你发现时用户已经看到乱码了。
> L123: ### Claude Code — 每次编辑自动触发

## 星数曲线

```mermaid
xychart-beta
    title "haodehaode378/text-encoding-guard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-25 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `52afe3f240ee` · [字段定义](../../DATASET.md)*
