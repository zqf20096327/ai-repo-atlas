# vahmoh/Veda

⭐ 95 · Rust · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/vahmoh/Veda) · [官网](https://www.vedaos.org) · 个人维护

**Rust 编写的桌面操作系统，内置语音 agent 控制**

用 Rust 从 UEFI 引导、微内核到窗口系统与应用完整实现的 x86-64 桌面操作系统。内置从开机启动的语音 agent：应用声明带类型的动作（内置超过 100 个），agent 通过与键鼠相同的代码路径操作所有应用；敏感或不可逆操作需用户同意。硬件驱动由运行在自有 hypervisor 上 VM 中的 Linux 承担，受 IOMMU 隔离、崩溃自动重启。含浏览器（WebKit）、OpenGL ES 3.0、防火墙、pkg 包管理等。需在 x86-64 Linux 上用 cargo 命令自行构建，可写入 USB 活动系统或 QEMU 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音 agent（可配置模型/语音/名称）通过类型化动作操作系统内所有应用
- 敏感与破坏性操作由系统强制征得用户同意
- Rust 微内核 + 自有 hypervisor 运行 Linux 驱动 VM（IOMMU 隔离，崩溃重启）
- 内置 100+ 应用动作、桌面应用套件与 pkg 签名包管理

## 适用场景

- 在 QEMU 或 x86-64 PC 上体验 agent 深度集成的桌面系统
- 通过语音让 agent 操作照片、音乐、文本编辑器等系统应用
- 参考其 ui 工具包为应用声明 agent 动作

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: An operating system written in Rust, with a voice agent built into the system.
> L21:  An agent in the system A service from boot that wakes when you say its name. Its model, its voice and even its nam
> L22:  Actions, not screen scraping Applications declare typed actions that run the same code as the keyboard and mouse. 

## 星数曲线

```mermaid
xychart-beta
    title "vahmoh/Veda 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-27"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-26 95 → 2026-10-27 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `828fb7951ba6` · [字段定义](../../DATASET.md)*
