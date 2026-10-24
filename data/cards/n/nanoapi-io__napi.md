# nanoapi-io/napi

⭐ 323 · TypeScript · NOASSERTION · 推送 2026-04-12 · [GitHub](https://github.com/nanoapi-io/napi) · [官网](https://nanoapi.io) · 组织维护

**离线代码架构分析 CLI：生成依赖清单并本地可视化**

面向开发者的全离线 CLI 工具：分析代码库的依赖、复杂度与结构，生成本地 JSON 依赖清单（含文件、符号、度量），并通过本地 Web 服务器提供 Cytoscape.js 交互式可视化。支持 Python、C#、C、Java（C++/PHP/JS/TS 开发中）。功能包括复杂度/耦合阈值审计、符号抽取重构、CI/CD 集成。AI 为可选功能：接入 OpenAI/Google/Anthropic 模型为依赖自动打标签，不使用时全程无 AI。通过安装脚本或 GitHub Releases 二进制安装，Windows 需经 WSL 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 生成含文件/符号/依赖/度量的 JSON 清单，按 commit 追踪架构历史
- 本地 Web 可视化：项目图、文件图、符号传递依赖链
- 复杂度/大小/耦合阈值审计与符号抽取重构
- AI 标签为可选功能，核心流程完全离线

## 适用场景

- 分析并可视化遗留代码库的依赖结构
- 在 CI/CD 中按 commit 生成清单跟踪架构演进
- 识别并抽取超阈值的符号做重构

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: `napi` is a fully offline CLI that analyzes your codebase's architecture --
> L24: - **🏷️ AI Labeling** (optional): Use OpenAI, Google, or Anthropic models to

## 星数曲线

```mermaid
xychart-beta
    title "nanoapi-io/napi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 322 --> 324
    line [323, 323]
```

2026-10-18 323 → 2026-10-24 323（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `7ce5b5bcb5f7` · [字段定义](../../DATASET.md)*
