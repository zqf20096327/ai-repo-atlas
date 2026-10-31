# Rin313/StegLLM

⭐ 23 · JavaScript · MIT · 推送 2026-06-11 · [GitHub](https://github.com/Rin313/StegLLM) · [官网](https://rin313.github.io/StegLLM/) · 个人维护 · 中文 README

**离线 LLM 文本隐写工具：把秘密信息伪装成普通文字**

离线运行的文本隐写程序：利用本地 LLM 将秘密信息编码为看似普通的文字，接收方可解密还原；流程包含压缩（Unishox 或 Deflate-Raw）与可选 ECC 加密。默认通过下载 zip 包以脚本方式运行（Windows 运行 windows.bat，Linux/macOS 运行 linux_mac.sh），可从 Hugging Face 等来源获取 gguf 文件替换 data 文件夹中的模型来自定义。另提供仅含解密功能的在线演示网页。README 声明仅供学习研究使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 离线运行，基于本地 gguf 模型（llama.cpp）
- 隐写流程含压缩（Unishox/Deflate-Raw）与可选 ECC 加密
- 支持替换 data 文件夹中的 gguf 模型自定义
- 提供仅解密功能的网页演示

## 适用场景

- 把秘密信息伪装成普通文字传递
- 研究 LLM 隐写与加密编码流程
- 接收方通过演示网页或本地程序解密还原信息

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: 一款离线的 AI 工具，能将你的秘密信息巧妙地伪装成一段普通文字。
> L23: 从 **Hugging Face** 等任何来源获取**gguf**文件，然后在项目目录的**data**文件夹中对 gguf 文件进行替换。

## 星数曲线

```mermaid
xychart-beta
    title "Rin313/StegLLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7183ddad2e9e` · [字段定义](../../DATASET.md)*
