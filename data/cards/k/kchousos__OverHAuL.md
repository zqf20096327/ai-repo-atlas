# kchousos/OverHAuL

⭐ 15 · Python · GPL-3.0 · 推送 2026-03-02 · [GitHub](https://github.com/kchousos/OverHAuL) · [官网](https://kchousos.com/BSc-Thesis/) · 个人维护

**用 ReAct 式 LLM agent 为 C 项目自动生成 libFuzzer harness**

面向 C 项目安全测试的 harness 自动生成系统：通过 ReAct 风格 LLM agent 与工具辅助推理，迭代构建与 libFuzzer 兼容的 fuzzing harness，全程无需人工干预。使用时配置 OpenAI API key，命令行传入仓库链接即可运行，生成的 harness 位于 output/ 目录。支持指定 commit、模型、目标文件与输出目录等参数。以 Python 包形式安装（需 Python>=3.10，git clone 后 pip install）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct 式 LLM agent 自动生成 libFuzzer 兼容 harness
- 迭代式构建，无需人工干预
- 支持指定 commit、模型与目标文件的命令行参数

## 适用场景

- 为自己的 C 项目快速生成可用的 fuzzing harness
- 降低 fuzzing 上手门槛，加速 C 代码安全测试

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: **OverHAuL** (*Harness Automation with LLMs*) is a system for automatically generating libFuzzer-compatible harness
> L65:     overhaul <repo-link>

## 星数曲线

```mermaid
xychart-beta
    title "kchousos/OverHAuL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a06d719284e9` · [字段定义](../../DATASET.md)*
