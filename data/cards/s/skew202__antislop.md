# skew202/antislop

⭐ 16 · HTML · 推送 2026-10-28 · [GitHub](https://github.com/skew202/antislop) · 个人维护

**检测 AI 生成代码遗留问题的多语言 linter，供开发者使用**

用 Rust 编写的命令行 linter，通过 tree-sitter AST 解析与正则混合模式，检测 AI 编码助手常留下的占位注释（TODO/FIXME）、拖延表述（for now）、含糊措辞（should work）、空函数桩与冗余注释。支持 17 种语言（其中 10 种为完整 AST+Regex 模式），提供 Core/Standard/Strict 三档 profile 与 antislop.toml 自定义模式，支持 LSP 与 GitHub Actions 集成。安装途径为 npm 或 cargo，另有预编译二进制。定位上与标准 linter 互补，不覆盖 eslint/clippy 默认可检出的规则。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- tree-sitter AST + 正则混合解析，17 种语言支持
- Core/Standard/Strict 三档 profile，Core 档声明零误报目标
- 支持 LSP 与 GitHub Actions CI 集成
- antislop.toml 自定义检测模式与文件扩展名

## 适用场景

- 我在 CI 流水线中拦截 AI 生成的占位符与桩代码
- 我想审计 AI 编码助手产出的代码完整度
- 日常开发中用 Standard 档检测拖延与含糊表述

## 场景标签

 · 领域:开发者工具/代码质量

## 证据(README 行号)

> L9: **A blazing-fast, multi-language linter for detecting AI-generated code slop.**
> L15: AI models often produce code that works but is littered with signs of hesitation or incompleteness. AntiSlop detect
> L35: * **AntiSlop**: Detects AI shortcuts (stubs, hallucinated API usage, hedging).

## 星数曲线

```mermaid
xychart-beta
    title "skew202/antislop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8d9a705f3f77` · [字段定义](../../DATASET.md)*
