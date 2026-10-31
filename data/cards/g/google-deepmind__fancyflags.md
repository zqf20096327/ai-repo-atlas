# google-deepmind/fancyflags

⭐ 35 · Python · Apache-2.0 · 推送 2026-06-10 · [GitHub](https://github.com/google-deepmind/fancyflags) · 组织维护

**扩展 absl.flags 的结构化命令行参数定义库**

DeepMind 维护的 Python 库，在 absl.flags 之上提供 dict、dataclass、可调用对象的类型化命令行参数（flag）：为每个字典项生成点分隔的覆盖 flag（如 replay.capacity），类型校验在错误进入程序前拦截。提供 DEFINE_auto（从函数签名推断）、DEFINE_from_instance（从实例值生成）、parser_overrides 与自定义 ff.Item 扩展机制。限定在 main 文件中使用，非依赖注入框架；auto 函数要求参数有类型注解且类型较简单。通过 pip 从 PyPI 或源码安装。

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

- dict/dataclass/可调用对象的结构化 flag 定义与点分隔命令行覆盖
- DEFINE_auto 从签名推断类型与默认值，DEFINE_from_instance 从实例生成
- 18 种 ff.Item 类型映射到对应 absl flag，可自定义扩展
- 与 abseil-py flagsaver 配合使用的说明

## 适用场景

- 为已有的构造函数或 dataclass 快速暴露命令行配置项
- 用嵌套点分隔 flag 覆盖实验配置中的单个字段
- 在测试中配合 flagsaver 安全覆盖结构化 flag 值

## 场景标签

 · 领域:软件开发工具/配置管理

## 证据(README 行号)

> L8: `fancyflags` is a Python library that extends
> L12: `fancyflags` provides flags corresponding to structures such as

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/fancyflags 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2f6a954e18db` · [字段定义](../../DATASET.md)*
