# prince776/LLM-Tor

⭐ 18 · TypeScript · AGPL-3.0 · 推送 2026-03-21 · [GitHub](https://github.com/prince776/LLM-Tor) · [官网](https://llmtor.com) · 个人维护

**匿名使用公网 LLM API 的隐私代理层：盲签名+Tor 切断身份关联**

面向公共 LLM API 的隐私保护代理：用户购买额度后由客户端生成盲令牌，服务端盲签名，客户端经 Tor 出口节点兑换令牌并发送请求，服务端验证后转发给 LLM，使代理方无法把用户身份与聊天内容关联。滥用检测通过两个长期盲签名令牌形成持久匿名假名，可封禁滥用者而不暴露真实身份。提供桌面客户端（从源码构建）与后端的 Docker 构建和 Azure 部署脚本。限制：不防护上游 LLM 提供商记录内容与全局网络攻击者；推理代理当前走标准 HTTPS，纯 Onion 部署为规划项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Blind RSA 盲签名令牌实现身份与用量的密码学解耦
- 客户端仅经 Tor 出口节点访问代理，单次令牌、不持久化聊天
- 基于盲签名双令牌的匿名假名滥用检测机制
- 提供后端 Docker 镜像与 Azure Container Apps 部署脚本

## 适用场景

- 通过公共 LLM API 时避免提示词与账号关联
- 以持久匿名假名使用 LLM 服务并接受滥用封禁机制
- 自托管隐私代理后端并部署到云端

## 场景标签

 · 领域:LLM 基础设施/隐私

## 证据(README 行号)

> L3: LLM-Tor is a privacy-preserving proxy layer for public LLM APIs.
> L24: 5. Server verifies signature and forwards to LLM.
> L26: The server cannot link usage to identity.

## 星数曲线

```mermaid
xychart-beta
    title "prince776/LLM-Tor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `242313544ac6` · [字段定义](../../DATASET.md)*
