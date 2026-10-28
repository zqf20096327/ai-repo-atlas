# cleanunicorn/earheart

⭐ 34 · JavaScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/cleanunicorn/earheart) · [官网](https://github.com/cleanunicorn/earheart/releases/latest) · 个人维护

**本地离线语音听写工具：一键热键把语音转文字贴进编码代理**

Electron 桌面听写应用：按全局热键说话，语音在设备端经 NVIDIA Parakeet TDT 0.6B v3（sherpa-onnx/ONNX Runtime，CPU 快于实时）转录，再由 Granite 4.0 Micro 在进程内清理语气词与口误，粘贴到当前焦点窗口（Claude Code、Codex、Cursor 等），无需集成或 API key，默认无账号、无遥测、音频不出本机。支持 Windows/macOS(Apple Silicon)/Linux，提供安装包、AppImage 与 deb；可选接入任意 OpenAI 兼容转录/聊天 API 或本地 earheart-stt 服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Parakeet TDT 0.6B v3 进程内本地转录（25 语言，CPU 快于实时）
- Granite 4.0 Micro 进程内清理，三种风格（Clean/Verbatim/Polished）可编辑提示词
- 粘贴到任意焦点窗口，无需集成、插件或 API key
- 技术名词词典纠正、暂停/恢复、本地 JSON 历史记录

## 适用场景

- 对终端里的 Claude Code/Codex 口述长提示词，替代打字
- 在邮件、笔记、issue 等任意文本框做离线语音听写
- 需要语音数据不出本机的隐私敏感场景听写

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L22: Earheart turns that part into talking. Press a global hotkey, say what you
> L132: - **Speech-to-text with NVIDIA Parakeet** — Parakeet TDT 0.6B v3 (multilingual,

## 星数曲线

```mermaid
xychart-beta
    title "cleanunicorn/earheart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cf7a4a554ef1` · [字段定义](../../DATASET.md)*
