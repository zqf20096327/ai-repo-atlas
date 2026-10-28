# Jiaye1998/duepocket

⭐ 22 · TypeScript · 推送 2026-06-08 · [GitHub](https://github.com/Jiaye1998/duepocket) · [官网](https://jiaye1998.github.io/duepocket/) · 个人维护 · 中文 README

**本地优先的续费/余额提醒 PWA，AI 辅助提取订阅信息**

面向个人用户的隐私优先记账提醒工具：以 IndexedDB 本地账本跟踪订阅、试用转付费与 App 余额，提前 30 天预警扣费。AI 部分包括一句话录入的结构化提取候选与本地 tesseract.js 截图 OCR，所有 AI 结果须经用户确认才入账；内置 50 样本双语评测集在运行时展示提取准确率。明确不含银行同步、账户登录或自动退订。另可打包为 headless Claude Code 技能，数据格式与 PWA 互通。

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

- 本地 IndexedDB 账本，无账号、无银行同步
- AI 提取候选 + 人工确认流程，本地 tesseract.js OCR
- 50 样本双语评测集在运行时展示提取准确率
- 可同时作为 Claude Code 技能运行，账本格式互通

## 适用场景

- 跟踪订阅和试用转付费，提前 30 天收到扣费预警
- OCR 截图或一句话录入订阅信息并确认入账
- 在 Claude Code 中用对话方式记录和查询续费雷达

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L11: It is designed as a privacy-first AI product engineering demo: no account, no bank sync, local IndexedDB storage, A
> L17: - AI-assisted one-line intake with structured extraction candidates

## 星数曲线

```mermaid
xychart-beta
    title "Jiaye1998/duepocket 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `751e31ae989a` · [字段定义](../../DATASET.md)*
