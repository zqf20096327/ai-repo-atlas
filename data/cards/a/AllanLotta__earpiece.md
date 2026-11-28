# AllanLotta/earpiece

⭐ 3 · JavaScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/AllanLotta/earpiece) · 个人维护

**给 Mac 通话用户的实时转录与答案提示工具**

macOS 菜单栏应用：监听麦克风与系统音频，在设备端完成语音转写、说话人分离与声纹识别，检测指向用户的问题并通过本机 Claude Code CLI 生成答案，显示在刘海区域。音频不出本机，仅转写文本发给 Claude；依赖 macOS 26+、Node 22+ 与已登录的 Claude 订阅，暂不支持 Intel Mac 与 Windows/Linux。每次通话输出 Markdown 转写与回顾。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端语音转写、说话人分离与声纹识别，音频不出本机
- 通过本机 Claude Code CLI 调用已有 Claude 订阅，刻意剥离 API key
- 答案显示在刘海区域，默认对屏幕共享隐藏
- 每次通话生成 Markdown 转写与回顾文件

## 适用场景

- 通话中被点名提问时实时看到可念出的回答
- 为每场会议留存转写稿与行动项回顾
- 不希望会议机器人入会或音频上传云端时记录通话

## 场景标签

`AI 助手` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L7: Earpiece listens to your calls on your Mac, transcribes them on-device, notices when a question is aimed at you
> L66:  transcript text goes to Claude, through the Claude Code CLI you already use.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `db60e3b11918` · [字段定义](../../DATASET.md)*
