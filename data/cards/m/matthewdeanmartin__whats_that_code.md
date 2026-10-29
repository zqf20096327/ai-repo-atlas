# matthewdeanmartin/whats_that_code

⭐ 24 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/matthewdeanmartin/whats_that_code) · [官网](https://whats-that-code.readthedocs.io/en/latest/) · 个人维护

**纯 Python 的源代码编程语言检测库**

以多分类器集成检测源代码所属编程语言的 Python 库：依次检查文件扩展名、shebang、关键词、正则模式计数、标准库解析（Python/JSON/XML/TOML）与标签，再用投票算法合并结果；可选开启 tree-sitter 语法解析（约 26 种语法）以提升无提示代码的准确率。无机器学习依赖，正则热路径使用 re2 并可回退到标准库 re。适用于扩展名/标签缺失或歧义时的兜底分类场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 集成扩展名/shebang/关键词/正则/解析器/标签多路证据投票
- 无机器学习依赖，纯 Python 实现
- 可选 tree-sitter 解析提升代码-only 准确率（约 13%→21%）
- re2 加速正则匹配，无 wheel 时自动回退标准库 re

## 适用场景

- 对无扩展名或标签歧义的代码片段做语言兜底识别
- 代码分析工具链中快速估算片段的编程语言
- 批量分类抓取到的源代码片段

## 场景标签

 · 领域:软件工程/源代码分析

## 证据(README 行号)

> L3: This is a Python programming language detection library.
> L5: It detects the programming language of source code with an ensemble of classifiers.
> L62: 1. Inspects file extension if available.

## 星数曲线

```mermaid
xychart-beta
    title "matthewdeanmartin/whats_that_code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `716f0f40465b` · [字段定义](../../DATASET.md)*
