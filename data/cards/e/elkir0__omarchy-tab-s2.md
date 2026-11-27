# elkir0/omarchy-tab-s2

⭐ 5 · Shell · GPL-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/elkir0/omarchy-tab-s2) · 个人维护

**在三星 Galaxy Tab S2 平板上运行的 64 位 Linux 系统移植，内置 AI 工具**

针对三星 Galaxy Tab S2 8.0 LTE（SM-T715）的 Omarchy 4.5 非官方移植：通过写入 PARAM 分区的自研引导器将仅支持 32 位内核的设备切换到 AArch64，在 Exynos 5433 八核上运行主线 Linux 6.12 与 Hyprland 桌面，并提供触摸 shell、LTE、Waydroid Android 应用支持。系统镜像内置 AI 组件：搜索栏直接调用 Claude Code、Claude Desktop、ChatGPT Desktop 等 AI 应用，Whisper 本地离线听写，以及 Ollama 本地模型（0.6B 约 10 token/s）。仅在一台参考设备上测试，SIM 功能在 64 位下未端到端验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自研 PARAM 引导器在每次启动时将 AArch32 切换为 AArch64，失败时回退到 bootloader 与救援镜像
- 主线 Linux 6.12 八核运行，含调频与热限策略
- 内置 AI 菜单：Claude Code、Claude Desktop、ChatGPT Desktop、Ollama、OpenCode、Grok 等，从官方源安装
- Whisper 离线听写针对该平板 CPU 重新构建，数据不出设备

## 适用场景

- 给闲置的 Galaxy Tab S2 装上现代 64 位 Linux 桌面当日常设备
- 在离线平板上用 Ollama 和本地听写处理语音与问答
- 学习 Exynos 5433 硬件的逆向与主线移植过程

## 场景标签

 · 领域:操作系统/硬件移植

## 证据(README 行号)

> L6: of its Exynos 5433, on mainline Linux 6.12, with **AI built in**: Claude Code one question away
> L32: - **AI, everywhere it fits.**
> L67: |AI|Claude Code, Claude Desktop, ChatGPT Desktop, mise, Ollama, OpenCode and Grok start on the tablet; dictation an


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `e62f8705f4f7` · [字段定义](../../DATASET.md)*
