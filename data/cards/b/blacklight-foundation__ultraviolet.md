# blacklight-foundation/ultraviolet

⭐ 25 · C++ · NOASSERTION · 推送 2026-07-03 · [GitHub](https://github.com/blacklight-foundation/ultraviolet) · [官网](https://ultraviolet-lang.org) · 组织维护

**面向人类与 AI 编写的通用系统编程语言（公开 alpha）**

由 Blacklight Foundation 开发的通用系统级编程语言，设计目标为显式权限、可预测执行与源码可读性，适用于人类编写、AI 生成、人类审阅的代码场景。语言特性包括基于能力的权限控制（无环境副作用）、模态类型（类型状态机）、作用域内存（Arena/Frame 分配器）与静态键并发系统。仓库含语言规范、C++ 自举编译器、运行时库与一致性测试套件。当前为 v0.1.0-alpha 公测版，官方声明勿作为成熟生产依赖；支持 Linux x86_64、Apple Silicon macOS 14+、Windows x86_64，提供命令行安装脚本与源码构建两种途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 能力（capability）权限模型：I/O、网络等副作用需显式句柄
- 模态类型将状态机与资源生命周期建模为语言级构造
- Arena/Frame 作用域内存管理与静态键并发系统
- 三平台（Linux/macOS/Windows）发布归档与 sha256 校验，安装器支持与 Python uv 命令共存

## 适用场景

- 评估一门为 AI 生成代码与人类审阅设计的系统编程语言
- 在 Linux/macOS/Windows 上试用自举编译器与一致性测试套件
- 参与语言规范评审或编译器/运行时贡献

## 场景标签

 · 领域:编程语言/开发工具

## 证据(README 行号)

> L21: Ultraviolet is a general-purpose systems programming language designed for **explicit authority**, **predictable ex
> L25: Ultraviolet is public alpha software. It is ready for inspection, early

## 星数曲线

```mermaid
xychart-beta
    title "blacklight-foundation/ultraviolet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c0d786a06474` · [字段定义](../../DATASET.md)*
