# zkwi/VoxType

⭐ 91 · Rust · MIT · 推送 2026-10-29 · [GitHub](https://github.com/zkwi/VoxType) · [官网](https://github.com/zkwi/VoxType/releases/latest) · 个人维护 · 中文 README

**Windows 隐私敏感型开源 AI 语音输入工具**

面向 Windows 10/11 用户的桌面语音输入工具：全局热键（默认 Ctrl+Q）触发，通过云端流式 ASR（默认豆包 bigmodel_async，可切换阿里云 FunASR Realtime）实时显示悬浮字幕，等待最终结果后可选调用 OpenAI 兼容大模型轻度润色，再写入剪贴板并自动粘贴。Rust/Tauri 负责系统能力，Svelte 提供配置与诊断界面；支持屏幕 OCR 上下文、自动热词、托盘常驻与开机启动。语音需发送至用户选择的云端 ASR 服务，需自备 API 凭据。

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

- 全局热键触发 + 悬浮实时字幕 + 最终结果门禁后自动粘贴
- 豆包流式 ASR（三种接入方式）与阿里云 FunASR Realtime 可切换
- 可选 OpenAI 兼容大模型轻度润色，带 min_chars 触发长度与思考模式适配
- 屏幕 OCR 上下文辅助识别专有名词，热词/上下文/统计等隐私边界明确

## 适用场景

- 在任意输入框用语音代替打字，中文/英文/混合输入
- 写邮件、聊天时对识别文本做大模型轻度润色后再粘贴
- 需要明确数据边界（不写日志、诊断脱敏、上下文默认关闭）的语音输入场景

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L20: **中文简介：** 把光标放到任意输入框，按下 `Ctrl + Q` 开始说话。VoxType 通过所选云端 ASR（默认豆包流式 ASR，也支持阿里云 FunASR Realtime）显示实时字幕，等待最终结果后可选调用 Ope
> L81: - 实时语音识别：默认对接豆包 `bigmodel_async` WebSocket，也可在 API配置页切换到阿里云 FunASR Realtime；字幕只作反馈，最终粘贴必须等待所选 ASR 服务返回最终完成事件。豆包链路继续

## 星数曲线

```mermaid
xychart-beta
    title "zkwi/VoxType 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 90 --> 92
    line [91, 91]
```

2026-10-18 91 → 2026-10-30 91（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `86d690e67cf7` · [字段定义](../../DATASET.md)*
