# gitrgoliveira/vault-plugin-secrets-openai

⭐ 25 · Go · MPL-2.0 · 推送 2026-10-07 · [GitHub](https://github.com/gitrgoliveira/vault-plugin-secrets-openai) · [官网](https://www.hashicorp.com/en/blog/managing-openai-api-keys-with-hashicorp-vault-s-dynamic-secrets-plugin) · 个人维护

**HashiCorp Vault 插件：动态创建与轮换 OpenAI API 密钥**

面向 Vault 的 secrets 引擎插件，通过 OpenAI Admin API 按需创建、轮换与撤销 OpenAI 项目服务账号及 API key，支持 TTL 配置、租约到期自动清理、admin key 手动与定时轮换，并输出 Prometheus 兼容指标。以 Go 编写，提供预编译二进制、make 源码构建与 Docker 容器化部署（仅 Linux 主机）三种方式。与 Vault 1.19.4 开发测试；README 声明 HashiCorp 不官方支持本插件、生产部署前需充分测试。仅支持动态服务账号凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按需动态生成 OpenAI 服务账号与 API key，支持 TTL/max_ttl
- 租约到期自动清理服务账号与密钥，admin key 可手动或定时轮换
- Prometheus 兼容的凭据签发/撤销/错误指标
- 提供预编译二进制、源码构建与 Docker（Linux）部署路径

## 适用场景

- 用 Vault 统一签发短期 OpenAI API 凭据给应用
- 自动轮换 OpenAI admin 根密钥降低泄露风险
- 对 OpenAI 凭据的签发与撤销做监控告警

## 场景标签

 · 领域:安全基础设施/密钥管理

## 证据(README 行号)

> L9: A HashiCorp Vault plugin for dynamic, secure management of OpenAI service accounts and API keys using the OpenAI Adm
> L20: - **Dynamic Service Accounts**: Create OpenAI service accounts with API keys. Configure TTLs for improved security.

## 星数曲线

```mermaid
xychart-beta
    title "gitrgoliveira/vault-plugin-secrets-openai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ffc305493075` · [字段定义](../../DATASET.md)*
