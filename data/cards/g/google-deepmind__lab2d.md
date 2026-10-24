# google-deepmind/lab2d

⭐ 445 · C++ · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/google-deepmind/lab2d) · 组织维护

**供强化学习/多智能体研究的 2D 网格世界环境构建系统**

用 C++ 与 Lua 编写的 2D 机器学习环境系统：通过文本地图定义世界布局、Lua 代码定义行为，生成网格世界环境；学习智能体经 Python dm_env API 或自定义 C API 与环境交互，支持多智能体。以 PyPI 预编译 wheel（Linux/macOS）分发，无对应 wheel 时需用 Bazel 从源码构建；系统需预装 Python 3.8+ 及 NumPy、PyGame、packaging。附随机智能体示例与可引用的 whitepaper。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本地图 + Lua 代码定义可定制网格世界环境
- 提供 Python dm_env API 与 C API 两种交互接口
- 支持多智能体环境
- PyPI 提供 Linux/macOS 预编译 wheel

## 适用场景

- 构建强化学习实验用的 2D 网格世界
- 多智能体交互研究的环境搭建
- 基于随机智能体示例快速预览与开发自己的 agent

## 场景标签

`强化学习` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: *DeepMind Lab2D* is a system for the creation of 2D environments for machine
> L13: Machine learning agents interact with these environments through one of two

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/lab2d 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 444 --> 446
    line [445, 445]
```

2026-10-18 445 → 2026-10-24 445（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `08e0d0122e6c` · [字段定义](../../DATASET.md)*
