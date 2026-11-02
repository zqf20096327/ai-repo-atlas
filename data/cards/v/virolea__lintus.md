# virolea/lintus

⭐ 12 · Rust · MIT · 推送 2026-09-23 · [GitHub](https://github.com/virolea/lintus) · 个人维护

**用自然语言写规则、由模型判定的代码检查工具**

Rust 编写的命令行 linter：从仓库根目录读取 YAML 规则文件，每条规则是一个关于文件的真/假问题（noul，带概率），连同文件路径与完整内容发送给 Jev 模型，概率超过阈值即报告 offense。支持全树、git diff、staged 文件检查，适配 CI 与 pre-commit 钩子，提供 GitHub Actions 集成与 text/github/json 输出格式。单二进制分发，需 Jev API key，可用 --list 不调 API 预览检查范围。

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

- 规则以自然语言问题形式写在 YAML 中，由模型带概率判定
- 支持全树/git diff/staged 三种文件范围，适配 CI 与 pre-commit
- 单二进制安装脚本，支持 Linux/macOS/Windows 多平台
- 提供 GitHub Actions 集成与 text/github/json 三种输出格式

## 适用场景

- 在 CI 中检查符合自然语言规范的架构约束
- 提交前用 pre-commit 钩子对 staged 文件做 lint
- 对'控制器不含业务逻辑'等难写成静态规则的约定做检查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: Lintus reads a YAML file of rules at the root of your repository. Each rule is a question
> L7: Jev model as a *noul* (a true/false judgement with a

## 星数曲线

```mermaid
xychart-beta
    title "virolea/lintus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-02"]
    y-axis "stars" 11 --> 13
    line [12, 12]
```

2026-10-18 12 → 2026-11-02 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `51f75f27746d` · [字段定义](../../DATASET.md)*
