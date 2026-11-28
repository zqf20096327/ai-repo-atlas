# gigaverse-app/dry-lint

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/gigaverse-app/dry-lint) · [官网](https://dry-lint.readthedocs.io/en/latest/) · 组织维护

**面向代码仓库的重复逻辑检测器：用 LLM 评审 PR 中的重复实现**

dry-lint 在 Python、TypeScript、Lua/Luau（含 Roblox）和 Lean 4 代码库中查找重复实现的函数：解析源码比对函数体，识别拉取请求中新写的、与既有代码功能相似的实现，再由 LLM judge 判定每对是否确为同一概念，结果以 PR 标注和评论回传。用户自带 API key，无 key 时仅列出相似对不做判定。支持 GitHub Actions 与 pre-commit 集成，提供 baseline 机制接受现存重复。通过 PyPI 分发，action 自带 Python 环境无需构建步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PR 中检测与既有代码功能重复的新实现并给出 judge 评分
- 无 API key 时仅列出相似对，不调用模型
- GitHub Actions 集成：PR 标注、sticky 评论、fork 模式拆分 detect/judge 作业
- 支持 Lean 4 证明重复片段扫描与 pre-commit 钩子

## 适用场景

- 在代码评审中拦截对既有 helper 的二次实现
- 监控 coding agent 产生的重复代码
- 用 pre-commit 在提交前检查重复逻辑
- Lean 项目中查找可共享引理的重复证明

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L36: dry-lint finds functions in a pull request that look like they re-implement something that already exists. A
> L48: **You bring your own keys.** dry-lint never provides API keys, models or judge execution: judges run on the


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `cd97f14efd88` · [字段定义](../../DATASET.md)*
