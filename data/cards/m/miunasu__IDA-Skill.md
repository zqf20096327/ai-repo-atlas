# miunasu/IDA-Skill

⭐ 238 · Python · AGPL-3.0 · 推送 2026-10-21 · [GitHub](https://github.com/miunasu/IDA-Skill) · 个人维护 · 中文 README

**让 AI Agent 用 IDA Pro 自动逆向分析恶意样本的技能包**

面向 AI Agent 的 IDA Pro 分析技能（SKILL.md 形式）：Agent 读取后可自动初始化 IDA 数据库、提取导入表/字符串/反编译代码、追踪调用链，并生成分析报告。内置三类工具：REAI（用 LLM 理解函数功能并自动重命名/注释，需配置 OpenAI/Azure/deepseek/本地模型 API）、FindCrypt（识别 AES/DES/RC4 等加密常量与哈希）、Export Check（检测 DLL 异常导出）。使用前需在 config.json 指定本机 IDA Pro 路径。GPL-3.0 且声明禁止商用，商用需联系作者授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent 读取 SKILL.md 后自动调用 IDA 完成逆向分析并生成报告
- REAI 用 LLM 理解函数功能、自动重命名函数与添加调用处注释
- FindCrypt 识别 AES/DES/RC4/Blowfish/TEA 等加密常量与 MD5/SHA 系列哈希
- 提取威胁指标：IP、域名、文件路径、注册表键值

## 适用场景

- 让 Claude 类 Agent 自动分析恶意样本并产出报告
- 自动化识别样本中的 C2 通信、进程注入与持久化机制
- 借助 LLM 自动理解与命名二进制函数、追踪调用链

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L9: 这是一个 **AI Agent skill**，让 AI 能够使用 IDA Pro 自动分析恶意软件，就像人类安全分析师一样：
> L37: 将 IDA Skill 放在你的skill文件夹即可。

## 星数曲线

```mermaid
xychart-beta
    title "miunasu/IDA-Skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 236 --> 239
    line [237, 238, 238]
```

2026-10-18 237 → 2026-10-29 238（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9ffcb18346d7` · [字段定义](../../DATASET.md)*
