# Asthestarsfalll/ExCore

⭐ 18 · Python · MIT · 推送 2026-04-27 · [GitHub](https://github.com/Asthestarsfalll/ExCore) · [官网](https://excore.onism.space/) · 个人维护 · 中文 README

**面向深度学习的配置与注册表系统，含实用工具**

面向深度学习训练流程的 Python 配置/注册表系统。将配置对象分为 Primary、Intermediate、Isolated 三类，扩展 TOML 语法（!、@、$、&、* 前缀）实现模块复用、类引用、变量引用与细粒度模型结构控制；提供 LazyConfig 延迟构建、模块参数校验、基于 LSP/JSON Schema 的配置文件自动补全与代码导航，以及 Registry 的延迟导入、模糊搜索等能力。附带 PathManager 路径管理插件。README 声明仍处于早期开发阶段，代码导航目前仅支持 neovim。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- TOML 扩展语法（!、@、$、&、*）支持模块复用、类引用与变量引用
- LazyConfig 延迟构建，load/build_all 两个 API 即可构建模块
- 配置文件支持自动补全、类型提示与代码导航（基于 LSP/JSON Schema）
- Registry 支持延迟导入、模块注册、模糊搜索与全局化

## 适用场景

- 深度学习训练项目中统一管理模型、优化器、数据集等超参数配置
- 通过配置继承与细粒度配置复用并组合模型结构
- 在编辑器中获得配置文件的补全、类型提示与类定义跳转

## 场景标签

 · 领域:深度学习基础设施

## 证据(README 行号)

> L3: `ExCore` is a Configuration/Registry System designed for deeplearning, with some utils.
> L21: Config System in `ExCore` is specifically designed for deeplearning training (generally refers to all similar part,

## 星数曲线

```mermaid
xychart-beta
    title "Asthestarsfalll/ExCore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0d6d65cf3239` · [字段定义](../../DATASET.md)*
