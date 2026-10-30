# sonpiaz/haynoi

⭐ 19 · Swift · MIT · 推送 2026-10-08 · [GitHub](https://github.com/sonpiaz/haynoi) · [官网](https://haynoi.com) · 个人维护

**macOS 越南语/英语混合听写工具，按键说话文字直达焦点应用**

面向越南语使用者的 macOS 按住即说（push-to-talk）听写应用：按住 ⌥ 键说话，松开后文字经转写直接插入当前焦点应用的光标处，支持越/英句中混说不互译。转写与 Email/Formal 改写由 Kyma API 云端完成（模型含 gpt-4o-mini-transcribe 与 whisper-v3-turbo），个人词典从用户纠正中学习且仅存本地。提供 DMG 安装包或源码构建，需 macOS 14+，Google 登录，免费档每周 5,000 词，Pro 版未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 越/英句中混说转写，不做翻译或合并
- 个人词典从纠正中学习，本地保存、重启保留
- Email/Formal 模式改写失败时仍插入原始转写
- 通过 Accessibility API 直接插入任意应用，带回退剪贴板

## 适用场景

- 在聊天、编辑器、浏览器里用语音输入越英混说的内容
- 用语音起草并自动润色成正式邮件
- 让专有名词和人名在多次听写后自动纠正

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3:  Push-to-talk dictation for macOS.
> L21: - **Speaks your language(s).** Vietnamese-optimized speech-to-text that handles Vi/En code-switching — and a person
> L92: **Runs on Kyma API.** Kyma handles speech-to-text and rewrite for every dictation so Haynoi never holds a model key

## 星数曲线

```mermaid
xychart-beta
    title "sonpiaz/haynoi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f197b549e3cd` · [字段定义](../../DATASET.md)*
