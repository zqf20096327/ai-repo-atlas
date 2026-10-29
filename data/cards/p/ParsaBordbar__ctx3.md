# ParsaBordbar/ctx3

⭐ 22 · Go · MIT · 推送 2026-09-05 · [GitHub](https://github.com/ParsaBordbar/ctx3) · 个人维护

**为开发者与 LLM 生成代码库结构化上下文的 Go CLI**

用 Go 编写的免费开源 CLI 工具，面向需要理解代码库的开发者与 LLM 使用场景：提供四个命令——context 输出文件大小、类型、依赖与 README 预览的元数据（支持 JSON）、print 打印文件层级、percentage 统计语言占比、pack 将整个仓库打包为单个 LLM 友好的 XML 文件（类似 Repomix），支持 glob 过滤、二进制处理、大小上限与正则脱敏。也可作为 Go 库导入使用。需安装 Go 工具链进行安装。

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

- ctx3 pack 将仓库打包为含目录结构与文件内容的单文件（XML）
- 支持 include/ignore glob、大小上限、二进制文件处理与正则脱敏
- context 命令输出 JSON 格式的文件与依赖元数据
- filetree/analyzer/pack 包可作为 Go 库复用

## 适用场景

- 把整个仓库打包成单文件粘贴给 LLM 分析
- 快速了解陌生项目的结构与语言构成
- 在 Go 项目中程序化获取代码库元数据

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Context Tree (ctx3)** is a free, open-source CLI tool written in Go that helps you (and your favorite LLM) unders
> L19: 3. **Pack** – generate a single, LLM‑friendly file that contains the directory structure and the full contents of f
> L76: **Why?** Handy for LLM workflows where you need to paste or upload a whole repo at once (similar to Repomix).

## 星数曲线

```mermaid
xychart-beta
    title "ParsaBordbar/ctx3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `171f432c9523` · [字段定义](../../DATASET.md)*
