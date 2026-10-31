# andrewkolagit/DetectPack-Forge

⭐ 24 · TypeScript · 推送 2026-03-19 · [GitHub](https://github.com/andrewkolagit/DetectPack-Forge) · [官网](https://detect-pack-forge.vercel.app) · 个人维护

**用自然语言或日志样本生成 SIEM 检测规则的 Web 应用**

面向 SIEM 学习者与安全从业者的 Web 应用：用户用英文描述行为或粘贴日志样本，前端向导（Vite+React）调用 n8n webhook，后端由两个 Gemini AI Agent 依次推断日志源 schema（含 MITRE ATT&CK 技术标签）并生成 Sigma、KQL（Sentinel）、SPL（Splunk）规则、正负测试样本与事件响应 playbook。产物可直接粘贴进 SIEM。前端本地运行无需 n8n；后端需自行导入仓库提供的 n8n workflow JSON 并配置 webhook URL。仓库未提供打包的桌面安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从行为描述或日志样本一次生成 Sigma/KQL/SPL 三种检测规则
- 附带正负测试样本与事件响应 playbook
- 自动映射 MITRE ATT&CK 技术标签
- 前端调用 n8n webhook，后端由 Gemini 双 Agent（schema 推断+产物生成）组成

## 适用场景

- 不熟悉各 SIEM 查询语法时以自然语言起草检测规则
- 为新观察到的高危行为快速产出多平台检测包
- 学习 SIEM 检测规则编写并获得可运行示例

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L8: You describe a behavior (e.g., “many failed logons then a success”) or paste a few log lines, and the app generates:
> L39: 3. 🧠 AI Agent – Schema (Gemini) infers:
> L49: 5. 🧪 AI Agent – Artifacts (Gemini) creates Sigma/KQL/SPL/tests/playbook from the schema + inputs.

## 星数曲线

```mermaid
xychart-beta
    title "andrewkolagit/DetectPack-Forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ac24a7419924` · [字段定义](../../DATASET.md)*
