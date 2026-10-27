# ashvardanian/TinySemVer

⭐ 30 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/ashvardanian/TinySemVer) · [官网](https://github.com/marketplace/actions/tinysemver) · 个人维护

**单文件 Python 的语义化版本发布工具，按 Conventional Commits 自动打 Git 标签**

面向遵循 Conventional Commits 规范的仓库的极简 SemVer 发布工具：读取提交动词（可自定义 major/minor 触发词）计算下一版本，更新版本号文件并推送 Git 标签，可作为命令行（pip/uvx 安装）或 GitHub Actions CI 使用。支持 -rc.N 发布候选、moving tags（v3/v3.0/v3.0.0，需 force-push 权限）、受保护分支的 PAT 安全注意事项。作者动机是用单文件替代约 363K 行 JavaScript 的 semantic-release。README 的 What's Missing 一节明确列出 GenAI 属于尚未支持的功能，optional commit scopes 亦未支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 Python 文件实现，提交动词到版本号与 Git 标签的自动化
- GitHub Actions 集成，支持多文件版本号正则更新（pyproject/package.json/CITATION.cff）
- 支持 -rc.N 发布候选与 major/minor 移动标签（默认关闭，需 force-push 权限）
- 文档含受保护分支下的 token 权限与安全风险说明

## 适用场景

- 在 CI 中按 Conventional Commits 自动计算并发布新版本标签
- 本地用 uvx --dry-run 预演下一版本号
- 维护 v3/v3.0/v3.0.0 式移动标签供 GitHub Actions 引用

## 场景标签

 · 领域:开发运维/发布工具

## 星数曲线

```mermaid
xychart-beta
    title "ashvardanian/TinySemVer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-27 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `09ef9a83987e` · [字段定义](../../DATASET.md)*
