# iurysza/herdr-tab-smart-rename

⭐ 78 · TypeScript · 推送 2026-10-22 · [GitHub](https://github.com/iurysza/herdr-tab-smart-rename) · 个人维护

**为 Herdr 终端生成任务感知的标签页与窗格名称的插件**

Herdr 终端的标签页/窗格命名插件：已知命令（如测试、开发服务器）通过规则直接命名，无需调用模型；其他任务将有限的终端上下文发送到用户选定的模型生成简短标签，后台自动更新。支持三种模型来源：OpenAI 兼容端点直连、复用已连接的 Pi provider、复用已安装 OpenCode 的 provider。手动设置的名称会被保留，弱证据时不变更名称。需 Herdr 0.7.5+ 与 Bun 1.2.23+，macOS/Linux 有安装脚本，Windows 走 Herdr 安装命令。敏感信息脱敏为尽力而为。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 已知命令规则命名，无需 AI 调用；其余任务由模型生成标签
- 三种模型来源：OpenAI 兼容直连 / Pi / OpenCode 复用已连接 provider
- 保留用户手动名称，弱证据不改名，窗格各自有标签

## 适用场景

- 在多标签多 agent 的终端里快速定位正在执行的任务
- 给共享同一标签的多个 agent 窗格分配独立标签
- 让终端标签名随当前工作内容自动更新

## 场景标签

 · 领域:终端/开发工具

## 证据(README 行号)

> L11: - Name known commands without an AI call. Use a model to interpret other tasks.

## 星数曲线

```mermaid
xychart-beta
    title "iurysza/herdr-tab-smart-rename 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-25 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2d6be56c5b08` · [字段定义](../../DATASET.md)*
