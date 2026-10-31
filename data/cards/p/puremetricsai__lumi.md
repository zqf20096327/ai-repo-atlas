# puremetricsai/lumi

⭐ 14 · Shell · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/puremetricsai/lumi) · [官网](https://lumimac.app) · 组织维护

**Mac 本地录屏录音并转录索引的记忆应用，供 AI agent 查询**

macOS 菜单栏应用，持续捕获屏幕截图、系统音频与麦克风，OCR、转录与索引均通过 Apple 自家框架在本地完成，数据不上传、无账号。本体不做任何 LLM 推理，而是通过 MCP 向 Claude Desktop、Claude Code、Cursor、Codex 等 agent 暴露 4 个只读工具（search_events/get_event/list_apps/get_transcript），由 agent 自带的模型回答关于用户工作记录的问题。要求 Apple Silicon + macOS 26，curl 脚本安装预构建应用，订阅制 $14/月，每日联网做更新检查与许可校验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 屏幕/系统音频/麦克风捕获 + 本地 OCR 与 Apple SpeechAnalyzer 转录，数据留在设备
- 通过 MCP 暴露 4 个只读查询工具，agent 自带模型、Lumi 不做推理
- 一键为 Claude Desktop/Claude Code/Cursor/Codex/Pi 配置 MCP 客户端
- 工具仅返回文本与元数据，不返回截图或录音

## 适用场景

- 录下整天的工作画面与会议，事后向 AI agent 提问检索
- 回溯几天前的报错信息、定价页或通话中提到的名字
- 根据真实记录生成周报或按应用统计时间去向

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L23: Lumi keeps the whole loop on your Mac. Capture, OCR, transcription, and the index all run locally with
> L26: inference at all; it hands your own searchable history to whichever AI agent you already trust.
> L135: This is how you ask Lumi what happened. Lumi serves its index to MCP-capable agents — Claude Desktop, Claude Code,

## 星数曲线

```mermaid
xychart-beta
    title "puremetricsai/lumi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `142f10319802` · [字段定义](../../DATASET.md)*
