# aSimmons5907/key-pool-rotator

⭐ 48 · C++ · MIT · 推送 2026-11-24 · [GitHub](https://github.com/aSimmons5907/key-pool-rotator) · [官网](https://github.com/aSimmons5907/key-pool-rotator/releases) · 个人维护

**为开发者聚合免费额度 LLM API 密钥池并自动轮换规避 429**

一个以原生 64 位 Windows 便携版发布的 LLM API 密钥池轮换工具：将多个免费额度的 LLM 提供商密钥汇入一个池，在遇到 429 限流时自动轮换密钥。配置由 config/settings.json 驱动，支持不重启的热加载；带环形缓冲管线、崩溃回滚的状态引擎与 stderr 遥测通道。无需编译即可使用预构建包运行，也提供 CMake 源码构建路径。面向使用多个免费层 API 密钥的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提供商免费额度 API 密钥池与 429 自动轮换
- config/settings.json 热加载配置，无需重启
- 预构建便携版，无编译器依赖
- 原子 JSON 状态与崩溃安全回滚

## 适用场景

- 把多个免费层 LLM API 密钥合并为一个入口使用
- 避免开发中频繁遭遇 429 限流中断
- 在 Windows 便携环境下运行密钥管理工具

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5:  LLM Key Rotator — Multi-Provider API Key Pool with Automatic 429 Rotation (One-Command Setup, Prebuilt Release): Po
> L20: **LLM Key Rotator — Pool your free-tier LLM keys, kill the 429s** (`key-pool-rotator`) ships as a native 64-bit Win

## 星数曲线

```mermaid
xychart-beta
    title "aSimmons5907/key-pool-rotator 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-26"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-11-25 48 → 2026-11-26 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `a6c3b74d069b` · [字段定义](../../DATASET.md)*
