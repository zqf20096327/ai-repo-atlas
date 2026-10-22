# tesserato/CodeWeaver

⭐ 746 · Go · MIT · 推送 2025-12-04 · [GitHub](https://github.com/tesserato/CodeWeaver) · 个人维护

**CLI 工具：把代码库合并为单个可导航的 Markdown 文档**

Go 编写的命令行工具，递归扫描目录生成树状文件结构，并将每个文件的完整内容嵌入 Markdown 代码块，输出单一 Markdown 文档。支持用正则表达式配置 include/ignore 黑白名单过滤路径，可将收录/排除路径保存到文件，并可复制到剪贴板。面向需要共享代码库、生成文档或为 AI/ML 工具准备输入的开发者。安装方式为 go install（需 Go 1.18+）或下载预编译可执行文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 递归扫描目录生成树状结构与完整文件内容嵌入的 Markdown
- 正则表达式 include/ignore 黑白名单路径过滤
- 收录/排除路径可导出到文件，支持复制到剪贴板
- 提供预编译可执行文件与 go install 两种安装方式

## 适用场景

- 把整个代码库打包成单个 Markdown 用于分享或存档
- 为 AI/ML 工具准备整合的代码库输入
- 生成带目录树的项目文档

## 场景标签

 · 领域:开发者工具/文档生成

## 证据(README 行号)

> L6: CodeWeaver is a command-line tool that transforms your codebase into a single, navigable Markdown document. It recur
> L12: * **Comprehensive Codebase Documentation:** Generates a Markdown file outlining your project's directory and file s

## 星数曲线

```mermaid
xychart-beta
    title "tesserato/CodeWeaver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 745 --> 747
    line [746, 746]
```

2026-10-18 746 → 2026-10-22 746（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1f034054f7c2` · [字段定义](../../DATASET.md)*
