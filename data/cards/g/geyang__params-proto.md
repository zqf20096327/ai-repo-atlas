# geyang/params-proto

⭐ 18 · Python · NOASSERTION · 推送 2026-02-05 · [GitHub](https://github.com/geyang/params-proto) · [官网](https://params-proto.readthedocs.io) · 个人维护

**声明式定义参数并自动生成 CLI 的 Python 装饰器库**

基于装饰器的轻量 Python 配置库：用类型注解与内联注释定义一次参数，即自动生成 CLI 解析、验证与带 ANSI 颜色的帮助文本。支持函数式与类式两种配置写法、@proto.prefix 前缀化配置组、命令行/Python 多种覆盖方式，以及 Literal/Union/Enum 复杂类型。当前为 v3 重设计版本（rc 预发布），通过 pip 安装，v2 旧 API 有迁移指南。面向需要管理机器学习超参数与命令行入口的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 装饰器定义参数即自动生成 CLI 解析、验证与帮助文本
- 支持函数式与类式配置及 @proto.prefix 前缀配置组
- Literal/Union/Enum 复杂类型支持
- v3 相对 v2 的迁移指南与文档体系

## 适用场景

- 机器学习训练脚本以类型注解方式声明超参数并生成命令行接口
- 用前缀配置组组织多模块（Agent/Environment）实验配置
- 替代手写 argparse/click 样板代码

## 场景标签

 · 领域:开发工具/机器学习配置

## 证据(README 行号)

> L1: # params-proto: Modern Declarative Parameters for Machine Learning
> L7: **params-proto** is a lightweight, decorator-based library for defining configurations in Python. Write your paramet

## 星数曲线

```mermaid
xychart-beta
    title "geyang/params-proto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `398d7a79e971` · [字段定义](../../DATASET.md)*
