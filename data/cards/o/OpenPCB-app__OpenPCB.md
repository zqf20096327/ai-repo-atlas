# OpenPCB-app/OpenPCB

⭐ 44 · TypeScript · AGPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/OpenPCB-app/OpenPCB) · [官网](https://openpcb.app/) · 组织维护

**桌面 PCB 设计套件：原理图、布局、DRC、制造输出一体**

跨平台 Electron 桌面应用，覆盖原理图绘制、PCB 布局（曼哈顿/45° 走线、过孔、 ratsnest）、设计规则检查（IPC-2221 间距、差分对等）、Gerber X2/Excellon 制造导出与统一元件库（含 200+ 器件，可导入 KiCad 符号与封装）。内置可选 AI 助手，可连接 OpenAI 或本地 Ollama/LM Studio 端点，能读取并修改设计，破坏性修改需用户批准，未配置前默认关闭。处于公开 beta，构建未签名。面向电子工程师与爱好者，双许可 AGPL-3.0 与商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 原理图到 Gerber/钻孔/BOM/贴片文件的一站式流程
- 与批处理检查共用内核的实时 DRC（IPC-2221B 间距与线宽估算）
- 200+ 元件库，支持导入 KiCad 符号/封装与 IPC-7351B 封装生成
- 可选 AI 助手连接 OpenAI 或本地 Ollama/LM Studio，破坏性修改需批准

## 适用场景

- 从原理图到制造文件的完整 PCB 设计，无需云端服务
- 用本地模型让 AI 助手读取并辅助修改自己的板子设计
- 按 IPC 规则检查间距、短路与线宽并导出给板厂

## 场景标签

 · 领域:电子设计自动化（EDA）/桌面工程软件

## 证据(README 行号)

> L3:  Modular, open desktop PCB design suite — schematic capture, PCB layout, design rule checking, manufacturing output 
> L78: **AI assistant.** Optional, and pointed at whichever provider you choose — OpenAI, or a local

## 星数曲线

```mermaid
xychart-beta
    title "OpenPCB-app/OpenPCB 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-26 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1a2993b8b255` · [字段定义](../../DATASET.md)*
